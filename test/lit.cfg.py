import os
import lit.formats
from lit.llvm.config import LLVMConfig
from lit.llvm.subst import ToolSubst

llvm_config = LLVMConfig(lit_config, config)

config.name = 'TinyMLIR'
config.suffixes = ['.mlir']
config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)
config.test_source_root = os.path.dirname(__file__)
config.test_exec_root = os.path.join(config.tiny_obj_root, 'test')

config.substitutions.append(('%PATH%', config.environment['PATH']))

# 将 tiny-opt 和 install/bin (含 FileCheck) 加入搜索路径
llvm_config.with_system_environment(['HOME', 'INCLUDE', 'LIB', 'TMP', 'TEMP'])
llvm_config.use_default_substitutions()

tools = ['tiny-opt', 'FileCheck']
tool_dirs = [config.tiny_tools_dir, config.llvm_tools_dir]
llvm_config.add_tool_substitutions(tools, tool_dirs)
