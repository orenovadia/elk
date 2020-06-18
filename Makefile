.PHONY:up
up:
	@docker-compose -f compose.yml up -d 

.PHONY:down
down:
	@docker-compose -f compose.yml down 

.PHONY:logs
logs:
	@docker-compose -f compose.yml logs -f 

.PHONY:open
open:
	@open 'http://localhost:5601/app/kibana#/dev_tools/console?_g=()' 


