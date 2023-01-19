name: coverage
  # run coverage
on: [push]
jobs:
  build:
    runs-on: macos-12
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.10.7'
      - name: install dependecies
        run: |
          pip install poetry
          poetry install
      - name: Code Climate Coverage Action
        uses: paambaati/codeclimate-action@v3.0.0
        env:
          DATABASE_URL: "sqlite://"
          CC_TEST_REPORTER_ID: 1f08027519bc9127bd09459d5e5910d1bfa2c7f9cd8569d7a155a63450b78dc3
        with:
          coverageCommand: make coverage
          debug: true
