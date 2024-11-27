#!/usr/bin/env python3
import os
import zlib

ROOT_DIR = os.path.join(os.path.dirname(__file__), '../')
CONNECTION_DEFLATE_PATH = os.path.join(ROOT_DIR,
                                       'mozc/src/data/dictionary_oss/'
                                       'connection.deflate')

CONNECTION_PATH = os.path.join(ROOT_DIR,
                                       'mozc/src/data/dictionary_oss/'
                                       'connection_single_column.txt')
MATRIX_DEF_PATH = os.path.join(ROOT_DIR, 'mecab-as-kkc/matrix.def')


def decompress_deflate(path):
    with open(CONNECTION_DEFLATE_PATH, 'rb') as f:
        return zlib.decompress(f.read()).decode()


def connection_open(path):
    with open(CONNECTION_PATH, 'rb') as f:
        return f.read()


def to_matrix(connections):
    num_classes = int(connections[0])
    connection_matrix = ['%s %s' % (num_classes, num_classes)]
    for lid in range(num_classes):
        for rid in range(num_classes):
            line = '%s %s %s' % (lid, rid,
                                 connections[lid * num_classes + rid + 1])
            connection_matrix.append(line)
    return '\n'.join(connection_matrix)


def main():
    connections = connection_open(CONNECTION_PATH)
    connections = connections.splitlines()
    connection_matrix = to_matrix(connections)
    with open(MATRIX_DEF_PATH, 'w') as f:
        f.write(connection_matrix)


if __name__ == '__main__':
    main()
