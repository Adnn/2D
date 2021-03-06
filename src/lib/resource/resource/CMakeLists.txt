project(resource)

set(AUTOGEN_DISCLAIMER "/* WARNING: Autogenerated file, do not edit directly */")
set(ASSET_FOLDER ${CMAKE_SOURCE_DIR}/assets)
configure_file(build_config.h.in build_config.h @ONLY)

set(${PROJECT_NAME}_HEADERS
    PathProvider.h
    #${CMAKE_CURRENT_BINARY_DIR}/build_config.h
)

add_library(${PROJECT_NAME} INTERFACE)

add_library(ad::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

# Custom target to have the files show up in the IDE
add_custom_target(${PROJECT_NAME}_IDE
    SOURCES
        ${${PROJECT_NAME}_HEADERS}
)

cmc_target_current_include_directory(${PROJECT_NAME})

target_include_directories(${PROJECT_NAME}
    INTERFACE
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}> # For generated header
)

target_link_libraries(${PROJECT_NAME}
    INTERFACE
        ad::platform)


##
## Install
##

install(TARGETS ${PROJECT_NAME} EXPORT ${PROJECT_NAME}Targets)

include(cmc-install)
# Install the header files
cmc_install_with_folders(DESTINATION include/${PROJECT_NAME}/${PROJECT_NAME}
                         FILES ${${PROJECT_NAME}_HEADERS})
# Prepare CMake package in both build and install trees
cmc_install_packageconfig(${PROJECT_NAME} ${PROJECT_NAME}Targets
                          NAMESPACE ad::)
