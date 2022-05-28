python_sources(name="src")

pex_binary(
    execution_mode="venv",
    name="main-non-docker",
)

pex_binary(
    execution_mode="venv",
    name="manylinux",
    entry_point="uvicorn",
    dependencies=[":src"],
    platforms=["manylinux_2_17_aarch64-cp-39-cp39"],
)

docker_image(
    name="docker",
    repository="{name}",
)
