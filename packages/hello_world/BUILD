python_sources(
    name="src"
)

pex_binary(
    execution_mode="venv",
    name="main-simple",
    entry_point="main.py",
)

pex_binary(
    execution_mode="venv",
    name="main",
    entry_point="gunicorn",
    platforms=["manylinux_2_17_aarch64-cp-39-cp39"],
)

docker_image(
    repository="{name}",
)
