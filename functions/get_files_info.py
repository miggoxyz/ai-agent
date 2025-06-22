import os
from google.genai import types


def get_files_info(working_directory, directory=None):
    working_directory = os.path.abspath(working_directory)
    directory = os.path.abspath(os.path.join(working_directory, directory))
    if not directory.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory {working_directory}'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    # - README.md: file_size=1032 bytes, is_dir=False
    items = [
        f"- {item}: file_size={os.path.getsize(os.path.join(directory, item))} bytes, is_dir={os.path.isdir(os.path.join(directory, item))}" for item in os.listdir(directory)]
    return "\n".join(items)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
