import tensorflow as tf

# linear_model: y = W*x + b
W = tf.Variable([.1], dtype=tf.float32)
b = tf.Variable([-.1], dtype=tf.float32)

x = tf.placeholder(tf.float32)

# create linear model
linear_model = W * x + b

y = tf.placeholder(tf.float32)

# create loss model
loss = tf.reduce_sum(tf.square(linear_model -y))

# create session use compute
sess = tf.Session()

# init variable
init = tf.global_variables_initializer()
sess.run(init)


# create a optimizer use Gradient Descent algorithm.
optimizer = tf.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)

# dataset
x_train = [1, 2, 3, 6, 8]
y_train = [4.8, 8.5, 10.4, 21.0, 25.3]

# Training 10,000 times
for i in range(10000):
    sess.run(train, {x: x_train, y: y_train})


# Print the results after training
print('W: %s b: %s loss: %s' % (sess.run(W), sess.run(b), sess.run(loss, {x: x_train, y: y_train})))
