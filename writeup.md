# CarND-Controls-PID
Self-Driving Car Engineer Nanodegree Program

---

## Algorithm description

I mostly followed the PID examples taught in class, with some minor modifications to pass the test. In short, the PID controller takes current CTE as input, computes three error terms: `p_error` for position error, `d_error` for derivative error and `i_error` for integral error. Each error is scaled by its respective gain `Kp`, `Kd` and `Ki` and summed. Then the control output will be the negative of the sum of errors. Here I only control the steering.

In order to evaluate the effectiveness of PID controller, I also injected a constant **steering bias**. Without the bias, PD controller works fairly well, but in the prescence of system bias, we can see that PID controller is able to minimize CTE to close to zero while PD controller can only converge to a nonzero CTE.

## Implementation

In `PID.h` I added the following variables:
```cpp
double cte; // previous cte value
double cte_sum;
double dt;
```

In `PID.cpp`, I set the cte initial value to a large negative value. This way, I can detect if it is the very first cte update and I will not compute the derivative term as there is no previous cte to calculate from. The rest is straight-forward.

In `main.cpp`, after receiving the current CTE, I simply pass it to the PID controller and get the returned steering input. I took care to convert it to range `[-1, 1]` by the `atan` function. Bias injection is also added here.

In order to visualize cte over time, I added all cte into a vector and dump them into a file at the end. Then I wrote a `visualize.py` to compare the performance of these controllers.

## Comparison of P, PD and PID controllers
![1](pic/1.png )

As can be seen, P controller has big oscillation behavior. And this manifests as ego car waving inside the lane. On the contrary, PD controller quicly converges to CTE=0 and follows the reference path closely. The P controller oscilates significantly and eventually veered off track (t=420).

When a system bias is present (steering bias=0.5), PD controller cannot converge CTE to zero. This causes the ego car to drive very close to the edge of the road. When it comes to a sharp turn, it sometime is not able to steer back in time and went off course. That is what happened at t=1200. PID controller, nevertheless, can correct the system bias and stay on track the whole time.

## Video recording

[![IMAGE ALT TEXT HERE]()](video/PID.mp4)
