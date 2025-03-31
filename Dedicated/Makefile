empire_cb: CB_MAPS_INIT.txt
	./build_config.py INIT_EMPIRE_CB_TEMPLATE.txt CB_MAPS_INIT.txt

empire_bt: ALL_MAPS_INIT.txt
	./build_config.py INIT_EMPIRE_BT_TEMPLATE.txt ALL_MAPS_INIT.txt

gor_sunday_event: ALL_MAPS_INIT.txt
	./build_config.py INIT_GOR_SUNDAY_EVENT_TEMPLATE.txt ALL_MAPS_INIT.txt

loyalist_base: ALL_MAPS_INIT.txt
	./build_config.py INIT_LOYALIST_BASE_TEMPLATE.txt ALL_MAPS_INIT.txt

ALL_MAPS_INIT.txt: $(wildcard ./MAPS/all_maps/*) ./MAPS/generate_maps2.py
	./MAPS/generate_maps2.py ./MAPS/all_maps/ Modules/Napoleonic\ Wars/ --init_file ALL_MAPS_INIT.txt

CB_MAPS_INIT.txt: $(wildcard ./MAPS/cb_maps/*) ./MAPS/generate_maps2.py
	./MAPS/generate_maps2.py ./MAPS/cb_maps/ Modules/Napoleonic\ Wars/ --init_file CB_MAPS_INIT.txt

all: ALL_MAPS_INIT.txt
cb: CB_MAPS_INIT.txt

clean:
	if [ -f INIT.txt ]; then rm INIT.txt ; fi
	if [ -f ALL_MAPS_INIT.txt ]; then rm ALL_MAPS_INIT.txt ; fi
	if [ -f CB_MAPS_INIT.txt ]; then rm CB_MAPS_INIT.txt ; fi

.PHONY: clean cb all gor_sunday_event empire_bt empire_cb
