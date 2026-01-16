What I implemented and why

For this assessment, I extended an existing SMS Spam Classification project with a focus on model lifecycle management and deployment safety rather than altering the core machine learning approach. The original implementation trained multiple models and exposed predictions via a FastAPI service, but it lacked mechanisms to control how and when new models are deployed. I implemented a baseline comparison and conditional deployment workflow using F1-score as the evaluation metric. This ensures that a newly trained model is promoted to production only if it demonstrates measurable improvement over the existing baseline, reflecting standard MLOps practices used in production ML systems to reduce performance regressions and deployment risk.

How to run the code

Install dependencies:

pip install -r requirements.txt


(Optional) Retrain the model by executing all cells in Spam Message Classification.ipynb, which generates the serialized model and tokenizer artifacts.

Run the evaluation and deployment gate:

python evaluate_and_compare.py


This script compares the new model’s F1-score with the stored baseline and updates the production model if the performance improves.

Start the FastAPI service:

uvicorn main:app --reload


Send a POST request to the /classify endpoint with an SMS message to receive a spam classification.

Assumptions and limitations

The baseline model’s performance is stored locally in a JSON file to simulate an existing production environment.

Model evaluation is intentionally simplified to highlight deployment logic rather than extensive experimentation.

The project does not include automated monitoring, CI/CD pipelines, or drift detection, but the structure allows these features to be added with minimal refactoring.

C. Reflection on Using a Coding Assistant

Using the coding assistant helped accelerate development by highlighting missing MLOps components and suggesting practical ways to introduce deployment safeguards. It was particularly useful in structuring the baseline comparison logic and clarifying how to separate training artifacts from production-serving artifacts. In some cases, suggested variable names or assumptions required manual verification against the actual codebase, reinforcing the importance of developer oversight. Debugging issues such as corrupted serialized models was a valuable learning experience and closely resembled real-world ML engineering challenges. Overall, the assistant was most effective as a conceptual and structural guide, while final implementation and validation decisions remained developer-driven. This experience emphasized the importance of combining tooling assistance with careful reasoning in production-oriented ML workflows.
