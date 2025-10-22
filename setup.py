"""Setup configuration for agent_demo package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agent_demo",
    version="0.1.0",
    author="Agent Demo Contributors",
    description="Demonstration of building AI agents using LangChain, LangGraph, and tool calling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/changsi/agent_demo",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "langchain>=0.3.7",
        "langchain-core>=0.3.15",
        "langchain-openai>=0.2.5",
        "langgraph>=0.2.45",
        "python-dotenv>=1.0.0",
    ],
)
