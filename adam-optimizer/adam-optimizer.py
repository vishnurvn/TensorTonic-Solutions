import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    grad = np.array(grad)
    
    m_t = beta1 * np.array(m) + (1 - beta1) * grad
    v_t = beta2 * np.array(v) + (1 - beta2) * np.square(grad)
    m_t_ = m_t / (1 - np.pow(beta1, t))
    v_t_ = v_t / (1 - np.pow(beta2, t))
    param = param - lr * m_t_ / (np.sqrt(v_t_) + eps)
    return param, m_t, v_t