Use *folder-generator.py* to generate folders on your machine

Use *json-generator.py* to generate jsons (provide all parameters manually in file)

*json-load.py* has first attempts of drawing networks

Use *ubuntu-folder-generator.py* to generate folders on lab laptop (tbh there's no need for a separate file, just run it directly on ubuntu)


## How to use json-generator

1. Go to *NSI-exemplary-problems* pdf file on Google Drive and find the problem you want to generate jsons for.
2. Assign numbers to the corresponding letters (p is 1, q is 2, etc.). As you fill the clauses, only the "idx" is needed for the program.
3. Each implication is a separate clause and each letter is a separate atom. You can add and delete them as you need, but remember to maintain the structure of the file.
4. So, for example, p /\ q -> r would look like that:
{
                            "tag": "Cl",
                            "clHead": {"idx": 3 , "label": ""},
                            "clPAtoms": [{"idx": 1, "label": ""}, {"idx": 2, "label": ""}],
                            "clNAtoms": [],
                        },
5. The rest of the parameters (bias, ahln and training data) can be found in Ch.2 of *NSI_MBR_ROME* pdf on google drive. These are the only ones manipulated as of now
6. Generated jsons file are meant to be put in the *experiment_versions* folder. To run the program, run the *__init__.py* script from  the terminal.



