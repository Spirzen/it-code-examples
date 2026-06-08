
import pulumi

from pulumi_aws import s3

import pytest

def test_bucket_has_versioning():
    # Отключаем реальное взаимодействие с AWS
    pulumi.runtime.set_mocks(MyMocks())

    # Импортируем модуль с инфраструктурой
    import infra

    # Проверяем, что бакет создан с версионированием
    bucket = infra.my_bucket
    assert bucket.versioning.enabled == True
