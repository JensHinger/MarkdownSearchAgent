from markdown_tools import * 
"""
tool_dict = {
    "Get files in a folder": get_files_in_folder,
    "Get folders in a folder": get_folders
}

ollama_tools = [
     {
        'type': 'function',
        'function': {
            'name': "Get files in a folder",
            "description": "This tool searches for files inside a folder relating to the keyword either because of the file name or the contents.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "Generate one keyword from the user request to search for in the folder structure"
                    },
                    "path": {
                        "type": "string",
                        "description": "The path for refining the search should only be the relative path from the initially provided root path"
                    }
                },
                "required": ["keyword", "path"],
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': "Get folders in a folder",
            "description": "This tool searches for folders inside a folder relating to the keyword due to the name of the folder.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "Generate one keyword from the user request to search for in the folder structure"
                    },
                    "path": {
                        "type": "string",
                        "description": "The path for refining the search should only be the relative path from the initially provided root path"
                    }
                },
                "required": ["keyword", "path"],
            },
        },
    },
]
"""

tool_dict = {
    "GetFilesAndFoldersInAFolder": get_files_and_folders
}

ollama_tools = [
     {
        'type': 'function',
        'function': {
            'name': "GetFilesAndFoldersInAFolder",
            "description": "This tool searches for files and folders inside a folder relating to the keyword either because of the file name, directory name or the contents.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "Generate one keyword from the user request to search for in the folder structure"
                    },
                    "path": {
                        "type": "string",
                        "description": "The path for refining the search should only be the relative path from the initially provided root path"
                    }
                },
                "required": ["keyword", "path"],
            },
        },
    }
]