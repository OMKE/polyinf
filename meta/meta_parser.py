import os
from pprint import pprint
from json import dump


class MetaParser:
    def __init__(self, path='./create-migration.sql', dump=True):
        self.path = path
        self.tables = self.parse()
        if dump:
            self.dump()

    def table(self, table_name: str):
        for table in self.tables:
            if table['name'] == table_name:
                return table

    def columns(self, table_name):
        return self.table(table_name)['columns']

    def primary_keys(self, table_name):
        return self.table(table_name)['primary_keys']

    def references(self, table_name):
        return self.table(table_name)['references']

    def dump(self, file_name='meta'):
        with open(f'meta/{file_name}.json', 'w') as file:
            dump(self.tables, file, ensure_ascii=False, indent=4)

    def parse(self):
        tables = []
        with open(self.path, 'r') as file:
            lines = []
            for line in file.readlines():
                table = {}
                line = self.__filter_line(line.strip("\n")).strip()
                if line != "":
                    lines.append(line)

            table = {}
            alter_lines = []
            alter_line = {}
            for line in lines:
                if "create table" in line:
                    table_name = line.split(" ")[-1].strip("`").strip("`")
                    table['name'] = table_name
                    continue
                if line == "(":
                    continue
                if line == ");":
                    # save the table and continue
                    tables.append(table)
                    table = {}
                    continue
                if "primary key" in line:
                    primary_key_line = [word.strip(
                        "(").strip(")") for word in line.split(" ")]
                    table['primary_keys'] = [
                        key.strip(",") for key in primary_key_line if key != "primary" and key != "key"]
                    continue
                if "alter table" not in line:
                    field_line = list(filter(len, line.split(" ")))
                    try:
                        column_name = field_line[0]
                        column_type = field_line[1]
                        additional_attrs = field_line[2:]
                        table['columns'].append({
                            'name': column_name.strip(","),
                            'type': column_type.strip(","),
                            'additional_attrs': [attr.strip(",") for attr in additional_attrs]
                        })
                    except KeyError:
                        table['columns'] = []
                        column_name = field_line[0]
                        column_type = field_line[1]
                        additional_attrs = field_line[2:]
                        table['columns'].append({
                            'name': column_name.strip(","),
                            'type': column_type.strip(","),
                            'additional_attrs': [attr.strip(",") for attr in additional_attrs]
                        })
                else:
                    line = line.split(" ")
                    alter_line['table'] = line[2]
                    alter_line['foreign_keys'] = [
                        key.strip("(").strip(")") for key in line[8:]]
                    alter_line['constraint'] = line[5]
                if "references" in line:
                    line = self.__filter_reference_line(line.split(" "))
                    alter_line['reference'] = line[0]
                    alter_line['reference_keys'] = line[1:]
                    alter_lines.append(alter_line)
                    alter_line = {}

            return self.__add_table_childs(tables, alter_lines)

    def __add_table_childs(self, tables: list, childs: list):
        for table in tables:
            for child in childs:
                if table['name'] == child['reference']:
                    try:
                        table['references'].append({
                            'name': child['table'],
                            'reference_keys': child['reference_keys'],
                            'constraint': child['constraint']
                        })
                    except KeyError:
                        table['references'] = []
                        table['references'].append({
                            'name': child['table'],
                            'reference_keys': child['reference_keys'],
                            'constraint': child['constraint']
                        })
        return tables

    def __filter_reference_line(self, line: list):
        words = [
            'on',
            'delete',
            'update',
            'restrict',
            'references'
        ]
        result = []
        for line_word in line:
            if line_word.strip(";") not in words:
                result.append(line_word)
        return [key.strip("(").strip(")") for key in result]

    def __filter_line(self, line: str):
        words = [
            "/*==============================================================*/",
            "drop table if exists",
            "DBMS name:",
            "Created on:",
            "/* Table: "
        ]
        result = line
        for word in words:
            if word == line or word in line:
                result = ""
        if result != None:
            return result
