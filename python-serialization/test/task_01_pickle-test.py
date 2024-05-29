#!/usr/bin/env python3
import sys
import os

# Ajouter le répertoire parent au chemin de recherche des modules
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
