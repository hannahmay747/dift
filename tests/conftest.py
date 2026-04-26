from pathlib import Path

import pytest


@pytest.fixture
def sample_csv_files(tmp_path: Path):
    old_csv = tmp_path / "old.csv"
    new_csv = tmp_path / "new.csv"

    old_csv.write_text(
        """customer_id,name,age,status,country,revenue
1001,Ama Mensah,28,active,Ghana,1200.50
1002,Kofi Asare,34,active,Ghana,850.00
1003,Esi Boateng,29,inactive,Ghana,0.00
1004,Yaw Owusu,41,active,Nigeria,2300.75
1005,Akosua Antwi,31,active,Ghana,1500.00
""",
        encoding="utf-8",
    )

    new_csv.write_text(
        """customer_id,name,age,status,country,revenue,segment
1001,Ama Mensah,28,active,Ghana,1350.00,Gold
1002,Kofi Asare,35,active,Ghana,850.00,Silver
1003,Esi Boateng,29,active,Ghana,120.00,Bronze
1005,Akosua Antwi,31,active,Ghana,,Silver
1006,Kojo Mensimah,26,pending,Kenya,620.40,New
""",
        encoding="utf-8",
    )

    return old_csv, new_csv
