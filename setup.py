import setuptools

setuptools.setup(
    name="tist",
    version="0.1.0.dev0",
    description="Todoist <-> Taskwarrior two-way sync",
    keywords="Todoist Taskwarrior",
    license="MIT",
    install_requires=[
        "setuptools",
        "Click",
        "todoist_api_python",
        "taskw",
    ],
    entry_points={
        "console_scripts": ["tist=tist.cli:cli"],
    },
)
