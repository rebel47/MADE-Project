import os
import pytest
import subprocess

# Directory path
data = '../data'
sqlite_file = os.path.join(data, "data.sqlite")

# Test setup to check file existence, handle accordingly, and run pipeline
@pytest.fixture(scope="module")
def setup_and_run_pipeline():
    # Check if the SQLite file exists
    if os.path.exists(sqlite_file):
        print(f"Found {sqlite_file}. Deleting the file.")
        os.remove(sqlite_file)
    else:
        print(f"{sqlite_file} does not exist. Running the pipeline directly.")

    # Run the pipeline
    print("Running pipeline.py...")
    result = subprocess.run(["python", "pipeline.py"], capture_output=True, text=True)

    # Check for errors in pipeline execution
    if result.returncode != 0:
        print("Pipeline execution failed:")
        print(result.stderr)
        pytest.fail("Pipeline execution failed.")

    yield  # Run tests after setup

# Test case: Verify the SQLite file is created
def test_pipeline_creates_sqlite(setup_and_run_pipeline):
    # Check that the SQLite file exists
    assert os.path.exists(sqlite_file), f"SQLite file not found: {sqlite_file}"
    print(f"{sqlite_file} verified successfully.")
