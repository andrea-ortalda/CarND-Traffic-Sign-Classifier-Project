# Solution is available in the "solution.ipynb" 
import tensorflow as tf

# Convert the following to TensorFlow:
x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.divide(x,y),tf.cast(tf.constant(1), tf.float64))

# Print z from a session
with tf.Session() as sess:
    output = sess.run(z)
    print(output)
