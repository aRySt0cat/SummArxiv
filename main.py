from arxive_collector import ArxivCollector


def main():
    collector = ArxivCollector("query.yaml")
    collector.collect()
    collector.save()


if __name__ == "__main__":
    main()
