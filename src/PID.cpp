#include "PID.h"

using namespace std;

/*
* TODO: Complete the PID class.
*/

PID::PID() : cte(-10000), cte_sum(0), dt(0.1) {}

PID::~PID() {}

void PID::Init(double _Kp, double _Ki, double _Kd) {
  Kp = _Kp;
  Ki = _Ki;
  Kd = _Kd;
}

void PID::UpdateError(double _cte) {
    
    p_error = Kp * cte;
    if (cte<-5000) // first measurement, no derivative yet
        d_error = 0;
    else {
        double delta_cte = _cte - cte;
        d_error = Kd * delta_cte / dt;
    }
    cte_sum += _cte;
    i_error = Ki * cte_sum;
    cte = _cte;
}

double PID::TotalError() {
    return p_error+d_error+i_error;
}

