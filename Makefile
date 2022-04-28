NAME=whiteboard
VERSION=latest
DOCKERBUILDARGS?=

build:
	docker build --build-arg react_app_build_env="local" -t $(NAME):$(VERSION) --rm .

django-settings-set:
	# Check $$DJANGO_SETTINGS_MODULE is set
	test -n "whiteboard.settings"

shell: django-settings-set build
	docker run --rm -it -e "DJANGO_SETTINGS_MODULE=whiteboard.settings" $(NAME):$(VERSION) sh

run: django-settings-set build
	docker run --rm -it   -e "DJANGO_SETTINGS_MODULE=whiteboard.settings" -e "PORT=8080" \
	-e "APP_ENV=local" -p 80:8080 -p 443:443 $(NAME):$(VERSION) /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf

audit:
	docker run --rm -it -v $(shell pwd)/frontend:/frontend -w /frontend node:dubnium-alpine npm audit --audit-level=moderate

audit-fix:
	docker run --rm -it -v $(shell pwd)/frontend:/frontend -w /frontend node:dubnium-alpine npm audit fix --audit-level=moderate

regenerate-package-lock:
	-rm frontend/package-lock.json
	docker run --rm -it -v $(shell pwd)/frontend:/frontend -w /frontend node:dubnium-alpine npm i --package-lock-only

build-frontend:
	docker run --rm -it -v $(shell pwd)/frontend:/frontend -w /frontend node:dubnium-alpine npm run build
	cp ./frontend/build/frontend/main.js ./whiteboard/static/frontend/main.js
	cp -rf ./frontend/build/frontend/* ./whiteboard/static

test-python: django-settings-set build
	docker run --rm -e "DJANGO_SETTINGS_MODULE=whiteboard.settings"   \
	-v $(shell pwd)/test-reports:/deploy/code/test-reports \
	-v $(shell pwd)/test-coverage:/deploy/code/test-coverage \
	$(NAME):$(VERSION) sh whiteboard/scripts/run_tests.sh

test-react:
	docker build $(DOCKERBUILDARGS) --build-arg react_app_build_env="local" -f Dockerfile.test -t $(NAME)-test:$(VERSION) --rm .
	docker run --rm \
	    -v $(shell pwd)/test-reports/frontend:/deploy/code/test-reports \
		-v $(shell pwd)/test-coverage/frontend:/deploy/code/coverage \
		$(NAME)-test:$(VERSION) sh /deploy/code/run_frontend_tests.sh

test: clean-test test-python test-react

get-logs:
	docker cp inventory_web_1:/var/log/supervisor/application.log ~/app.log

black: build
	docker run -it -e "DJANGO_SETTINGS_MODULE=whiteboard.settings"  $(NAME):$(VERSION) black --check .

safety:
	docker run --rm  -v $(shell pwd):/safety pyupio/safety safety check -r /safety/requirements.txt --full-report

clean-test:
	rm -rf test-reports test-coverage

clean-frontend:
	rm -r whiteboard/static/* || echo "No static content"

clean: clean-test clean-frontend
	# preceding dash is to prevent the makefile from erroring if the file/image doesn't exist
	# see: https://superuser.com/a/523510/150897
	-docker rmi $(NAME):$(VERSION)
	-docker rmi $(NAME)-test:$(VERSION)
