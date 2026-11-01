from lib import mcq, Q, OR

AR_OPTS = ["Both A and R are true and R is the correct explanation of A",
           "Both A and R are true but R is not the correct explanation of A",
           "A is true but R is false",
           "A is false but R is true"]

def AR(a, r, ans, why):
    return mcq(f"<b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}", list(AR_OPTS), ans, why)
