USE SCHEMA {{ params.schema }};

put file://{{ params.path_file }} @{{ params.stage }} auto_compress=true;