import json
from typing import Annotated, Any
from mcp.server.fastmcp import FastMCP, Context
from codegen import Codebase
from codegen.sdk.codebase.span import Span
from codegen.cli.api.client import RestAPI
import codegen
# Initialize FastMCP server
mcp = FastMCP("codegen-mcp")



def get_codebase_path(dir_path: str) -> Codebase:
    """Get the path to the codebase."""
    codebase = Codebase(dir_path)
    return codebase


@mcp.resource("config://service", mime_type="application/json")
def get_service_config() -> dict[str, Any]:
    """Get the service config."""
    return {
        "name": "codegen-mcp",
        "version": "0.1.0",
        "description": "A service for generating codemods for a given task and codebase using the codegen sdk",
    }

# @mcp.tool()
# def get_all_functions_in_filepath(codebase_path: Annotated[str, "The absolute path to the codebase directory"], file_path: Annotated[str, "The codebase relative path to the file to get functions from"]) -> list[str]:
#     """Get all functions in the codebase."""
#     codebase = get_codebase_path(codebase_path)
#     file =  codebase.get_file(file_path)

#     return [func.span for func in file.function_calls]


# @mcp.tool()
# def get_all_usages_for_symbol(codebase_path: Annotated[str, "The absolute path to the codebase directory"], symbol_name: Annotated[str, "The name of the symbol to get usages for"]) -> list[str]:
#     """Get all files in the codebase, given the absolute path to codebase directory and the name of the symbol"""
#     codebase = get_codebase_path(codebase_path)
#     target = codebase.get_symbol(symbol_name)

#     if hasattr(target, 'usages'):
#         return [usage.usage_symbol.span for usage in target.usages]
#     else:
#         return []


@mcp.tool()
def generate_codemod(task: Annotated[str, "The task to which the codemod should implement to solve"], codebase_path: Annotated[str, "The absolute path to the codebase directory"], ctx: Context) -> str:
    """Generate a codemod for the given task and codebase."""
    codebase = get_codebase_path(codebase_path)
    language = codebase.language
    return f'''use the codegen cli and run the following command:
          
          codegen create generate-codemod -d "{task}"
          
    '''


@mcp.tool()
def get_codemod_for_prompt(prompt: Annotated[str, "The task to which the codemod should implement to solve"], include_files: Annotated[list[str], "The files to include in the codemod"], exclude_files: Annotated[list[str], "The files to exclude from the codemod"], ctx: Context) -> str:
    """Get the path to the codebase."""
    codebase = Codebase(codebase_path)
    return codebase.path


@mcp.tool()
def improve_codemod(
    codemod_source: Annotated[str, "The source code of the codemod to improve"],
    concerns: Annotated[list[str], "A list of issues that were discovered with the current codemod that need to be considered in the next iteration"],
    context: Annotated[dict[str, Any], "Additional context for the codemod this can be a list of files that are related, additional information about the task, etc."],
    ctx: Context
) -> str:
    """Improve the codemod."""
    return f'''use the codegen cli and run the following command:
          
          codegen create improve-codemod -d "{codemod_source}"
          
    '''

if __name__ == "__main__":
    # Initialize and run the server

    print("Starting codegen server...")
    mcp.run(transport='stdio')
