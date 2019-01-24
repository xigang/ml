import numpy as np
import tensorflow as tf

# create feature columms list
feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]

# create linear regressor use train a linear regression model
estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

# save train dataset
x_train = np.array([1., 2., 3., 6., 8.])
y_train = np.array([4.8, 8.5, 10.4, 21.0, 25.3])

# save eval dataset
x_eval = np.array([2., 5., 7., 9.])
y_eval = np.array([7.6, 17.2, 23.6, 28.8])


#create an input model with training data for later model training
train_input_func = tf.estimator.inputs.numpy_input_fn(
        {"x": x_train}, y_train, batch_size=2, num_epochs=None, shuffle=True)


# Create an input model with training data for subsequent model evaluation
train_input_func_two = tf.estimator.inputs.numpy_input_fn(
        {"x": x_train}, y_train, batch_size=2, num_epochs=1000, shuffle=False)

eval_input_func = tf.estimator.inputs.numpy_input_fn(
        {"x": x_eval}, y_eval, batch_size=2, num_epochs=1000, shuffle=False)

# Train 1000 times using training data
estimator.train(input_fn=train_input_func, steps=1000)

#Evaluate the model using the original training data to see the results of the training
train_metrics = estimator.evaluate(input_fn=train_input_func_two)
print("train metrics: %r" % train_metrics)

#Evaluate the model using the evaluation data to verify the generalization performance of the model
eval_metrics = estimator.evaluate(input_fn=eval_input_func)
print("eval metrics: %s" % eval_metrics)
