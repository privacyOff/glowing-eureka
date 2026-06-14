class SearchEvaluator:

    def top1_accuracy(
        self,
        evaluations,
    ) -> float:

        correct = 0

        for item in evaluations:

            if (
                item.predicted[0]
                in item.relevant
            ):
                correct += 1

        return (
            correct
            / len(evaluations)
        )

    def top5_accuracy(
        self,
        evaluations,
    ) -> float:

        correct = 0

        for item in evaluations:

            if any(
                prediction
                in item.relevant
                for prediction in item.predicted[:5]
            ):
                correct += 1

        return (
            correct
            / len(evaluations)
        )

    def mean_reciprocal_rank(
        self,
        evaluations,
    ) -> float:

        scores = []

        for item in evaluations:

            rank = None

            for idx, prediction in enumerate(
                item.predicted,
                start=1,
            ):

                if (
                    prediction
                    in item.relevant
                ):
                    rank = idx
                    break

            scores.append(
                0
                if rank is None
                else 1 / rank
            )

        return (
            sum(scores)
            / len(scores)
        )