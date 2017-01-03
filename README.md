# treeviz

Decision Tree visualization for Spark ML (version 1.6.2) and Scikit-learn decision tree classifiers using D3.js

## Spark ML

```
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import DecisionTreeClassifier

from treeviz.spark_tree import tree_to_json
from treeviz.tree_rendering import render_tree

# Spark ML Decision Tree model sample
assembler = VectorAssembler(
    inputCols=model_variables,
    outputCol='features'
)

target_indexer = StringIndexer(
    inputCol='target',
    outputCol='target_index'
)

dt = DecisionTreeClassifier(
    labelCol='target_index',
    featuresCol='features',
    maxDepth=params['max_depth']
)

pipe = Pipeline(
    stages=[
        target_indexer,
        assembler,
        dt
    ]
)
model = pipe.fit(df_train)
```

## Scikit-learn

```
from sklearn import tree
from dataviz.sklearn_tree import tree_to_json

clf = tree.DecisionTreeClassifier(max_depth=params['max_depth'], random_state=params['seed'])
model = clf.fit(df[features], df['target'])

tree_to_json(model, features, target, 'testing_sklearn_tree.json')
render_tree('testing_sklearn_tree.json')
```
