# Import DeepEval test case object
from deepeval.test_case import LLMTestCase

# Import Faithfulness metric
from deepeval.metrics import FaithfulnessMetric


def evaluate_answer():

    # Context from retrieved document
    context = [
        """
        Password Reset Policy

        Employees can reset passwords using the
        self-service portal.

        Steps:

        1. Open Security Settings.
        2. Select Reset Password.
        3. Verify identity using MFA.
        4. Create a new password.
        """
    ]

    # Simulated LLM answer
    answer = """
    Employees can reset passwords by opening
    Security Settings, selecting Reset Password,
    verifying identity with MFA,
    and creating a new password.
    """

    # DeepEval test case
    test_case = LLMTestCase(
        input="How do I reset my password?",
        actual_output=answer,
        retrieval_context=context
    )

    # Faithfulness metric
    metric = FaithfulnessMetric(
        threshold=0.7
    )

    # Run evaluation
    metric.measure(test_case)

    print("\nFaithfulness Score:")
    print(metric.score)

    print("\nReason:")
    print(metric.reason)

    print("\nPass:")
    print(metric.is_successful())


if __name__ == "__main__":
    evaluate_answer()