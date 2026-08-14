# 替换 @变量@ 生成 build 目录下的 lit 站点配置
configure_lit_site_cfg(
    ${CMAKE_CURRENT_SOURCE_DIR}/lit.site.cfg.py.in
    ${CMAKE_CURRENT_BINARY_DIR}/lit.site.cfg.py
    MAIN_CONFIG
    ${CMAKE_CURRENT_SOURCE_DIR}/lit.cfg.py
)

# 依赖工具：tiny-opt，外部工具依赖 FileCheck
add_custom_target(check-tiny
    COMMAND ${LLVM_EXTERNAL_LIT} -v ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS tiny-opt
    COMMENT "Running TinyMLIR-GPU lit test suite..."
)
