import os
from functools import partial
from os.path import isfile, join
from typing import Optional

# from sys import stderr
from django.db.models import FileField, Model
from django.forms import Field

from history import settings
from history.forms import SourceFileFormField
from history.structures.source_file import TextualSourceFile


def dedupe_files(path: str, new_file_name: Optional[str] = None):
    full_path = f'{settings.MEDIA_ROOT}/{path}'
    if not new_file_name:
        raise NotImplementedError
    else:
        # If uploading a new file, replace an older version if one exists.
        # TODO: Ensure this doesn't result in replacements of unrelated files that happen to have the same name.
        new_file_name, extension = os.path.splitext(new_file_name)
        file_names = []
        for f in os.listdir(full_path):
            if isfile(join(full_path, f)) and extension in f:
                file_name = f.replace(extension, '')
                file_names.append(file_name)
        to_remove = []
        for file_name in file_names:
            if file_name == new_file_name:
                full_file_name = f'{file_name}{extension}'
                file_path = f'{os.path.join(path, full_file_name)}'
                to_remove.append(file_path)
        for file_path in to_remove:
            print(f'Removing old version of {file_path} ...')
            os.remove(f'{settings.MEDIA_ROOT}/{file_path}')


def _update_filename(instance: Model, filename: str, path: str):
    path, filename = path, filename
    filename = filename.replace(' ', '_')
    dedupe_files(path, new_file_name=filename)
    return os.path.join(path, filename)


def upload_to(path):
    return partial(_update_filename, path=path)


class SourceFileField(FileField):
    attr_class = TextualSourceFile

    def formfield(self, **kwargs) -> Field:
        return super(FileField, self).formfield(**{
            'form_class': SourceFileFormField,
            **kwargs,
        })
