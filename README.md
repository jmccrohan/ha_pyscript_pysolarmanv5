# ha_pyscript_pysolarmanv5

This is a [PyScript](https://github.com/custom-components/pyscript) wrapper for [pysolarmanv5](https://github.com/jmccrohan/pysolarmanv5) to provide easy integration with
[Home Assistant](https://www.home-assistant.io).

## Instructions

- Install pyscript from [HACS](https://hacs.xyz/)
- Clone/extract `ha_pyscript_pysolarmanv5` directory to `/config/pyscript/apps/`
- Add the following to `configuration.yaml`:
```
pyscript:
  allow_all_imports: true
  apps:
    ha_pyscript_pysolarmanv5:
      address: "192.168.1.200"
      serial: 12345667867
      port: 8899
```
- Call services from within HA as required:
`pyscript.pysolarmanv5_write_multiple_holding_registers`
