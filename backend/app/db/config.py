# MongoDB's connection details
import os

MONGO_URI = "mongodb+srv://s2606445:Carlson@cluster0.lckhdjd.mongodb.net/psd?retryWrites=true&w=majority&appName" \
            "=Cluster0"
MONGO_TEST_URI = "mongodb+srv://s2606445:Carlson@cluster0.lckhdjd.mongodb.net/test?retryWrites=true&w=majority" \
                 "&appName=Cluster0"

# The name of the database to use
TEST_MODE = os.environ.get("TEST_MODE", "True") == "True"

print("Test Mode: ", TEST_MODE)
