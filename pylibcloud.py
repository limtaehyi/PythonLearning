from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# amazon EC2 인스턴트 생성
# !! -- https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials/access-key-wizard -- !!
ACCESS_ID = 'your_access_key'
SECRET_KEY = 'your_secret_key'

cls = get_driver(Provider.EC2)
driver = cls(ACCESS_ID, SECRET_KEY)

sizes = driver.list_sizes()
print(sizes)

image = driver.list_images()[0]
size = sizes[0]

node = driver.create_node(name='test_node', image=image, size=size)
print(node)


# amazon S3 버킷 생성
ACCESS_ID = 'your_access_key'
SECRET_KEY = 'your_secret_key'

cls = get_driver(Provider.S3)
driver = cls(ACCESS_ID, SECRET_KEY)

container = driver.create_container(container_name='my_bucket')
print(container)

#CDN 서비스 cloudflare 도메인 추가
EMAIL = "your_cloudflare_email"
API_KEY = "your_cloudflare_key"
subdomain = "www.example.com"

cls = get_driver(Provider.CLOUDFLARE)
driver = cls(EMAIL, API_KEY)

zone = driver.create_zone(subdomain)
print(zone)

#컨테이너 서비스 도커 이미지 가져오기 및 실행
from libcloud.container.types import Provider
from libcloud.container.providers import get_driver
import os

cls = get_driver(Provider.DOCKER)
driver = cls(host='https://127.0.0.1', port=2375, key_file=os.path.expanduser('~/.ssh/id_rsa'))

image = driver.install_image('ubuntu:latest')
container = driver.deploy_container('test_container', image)
