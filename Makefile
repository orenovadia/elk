.PHONY:help
help:   ## Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY:up
up:     ## Run elastic+kibana (background)
	@docker-compose -f compose.yml up -d 

.PHONY:down
down:   ## Stop the containers
	@docker-compose -f compose.yml down 

.PHONY:logs
logs:   ## Follow the logs 
	@docker-compose -f compose.yml logs -f 

.PHONY:open
open:   ## Open a browser window on Kibana
	@open 'http://localhost:5601/app/kibana#/dev_tools/console?_g=()' 


