import ollama
from model_description import *
from tool_descriptions import ollama_tools, tool_dict
from model_description import *

PATH = "E:/KnowledgeVault/"

user_input = input("What would you like to search for? \n")

messages = [{"role": "system", 
             "content":f'''
                Tasks: Find relevant files concerning a topic provided by the user
                You are able to use a tool with the name: "GetFilesAndFoldersInAFolder"
                which requires two parameters the keyword to search for is provided by the user in the first query and
                the path in which to serach is {PATH}.
                Both of these parameters are required for the search to be done. Otherwise the tool will return an appropriate error.
                
                It can be used to get all relevant file- and foldernames inside a certain folder.
                In most cases it will be necessary to call the tool more than once. This should happen when no file is returned that is related to the topic.
                Further searches should be done using previously folders returned by the tool call for the next tool call.

                If the tool output is folders and files, check first if any file seems relevant enough to the query, if so return this file to the user.
                If the tool output contains folders, continue calling the available tool with a folder that is closest to the initial user query.
                If the tool output only contains files, check if any file is relevant enough to the query, if so return this file to the user.
                If no files fit the user query you can either try other folders whichh were discovered earlier or tell the user that there is no file related to the initial query.
            '''}
            ,{"role": "user", "content": f"{user_input}"}]

for i in range(5):
    response: ollama.ChatResponse = ollama.chat(
        MODEL_NAME,
        messages=messages,
        tools=ollama_tools
    )

    print(response["message"]["content"])

    print(response.message.tool_calls)
    if response.message.tool_calls:

        for tool_call in response.message.tool_calls:
            if function_to_call := tool_dict.get(tool_call.function.name):
                print("Calling tool: ", tool_call.function.name, " \n with arguments: ", tool_call.function.arguments)

                tool_res = function_to_call(**tool_call.function.arguments)

                if type(tool_res) == str:
                    print("Error ", tool_res)
                    messages.append({
                    "role": "tool", 
                    "content": f"An error occurend with the following message: {tool_res}"})
                else:
                    print(" Tool response is ", tool_res)
                    messages.append({
                        "role": "tool", 
                        "content": f'''
                            Here is the tool output:
                            files {", ".join(tool_res["files"])}
                            folders {", ".join(tool_res["folders"])}
                        '''})
            else:
                print("No tool with that name exists")
    else:
        print("No tool calls returned from the model")