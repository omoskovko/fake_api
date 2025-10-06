import pytest
from .common import get_request, post_request


@pytest.mark.parametrize(
    "endpoints",
    [
        {"name": "users"},
        {"name": "products", "params": {"inStock": "true"}},
        {"name": "orders"},
    ],
    indirect=True,
    ids=lambda c: c["name"],
)
@pytest.mark.parametrize(
    "dataset",
    [
        {"type": "GET"},
        {"type": "POST"},
    ],
    indirect=True,
    ids=lambda d: d["type"],
)
def test_client_over_datasets(endpoints, dataset, post_template, all_db):
    if dataset["type"] == "GET":
        res = get_request(endpoints["url"], params=endpoints["params"])
        assert res["status"] == "OK"

        all_dataset = all_db[endpoints["name"]]
        orig_data = [
            a == r for a in all_dataset for r in res["result"] if a["id"] == r["id"]
        ]
        assert len(orig_data) == len(res["result"])
        assert all(orig_data)
    else:
        if endpoints["name"] not in post_template:
            pytest.skip("Not supported")

        res = post_request(endpoints["url"], data=post_template[endpoints["name"]])
        assert res["status"] == "OK"
        for key in post_template[endpoints["name"]]:
            assert key in res["result"]
            assert post_template[endpoints["name"]][key] == res["result"][key]
