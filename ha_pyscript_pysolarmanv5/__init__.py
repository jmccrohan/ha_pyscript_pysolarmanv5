from pysolarmanv5 import PySolarmanV5

retry_attempts = pyscript.app_config.get("retry_attempts", 3)

address = pyscript.app_config.get("address", "solis")
serial = pyscript.app_config.get("serial", 1234567890)
port = pyscript.app_config.get("port", 8899)
mb_slave_id = pyscript.app_config.get("mb_slave_id", 1)
socket_timeout = pyscript.app_config.get("socket_timeout", 60)
v5_error_correction = pyscript.app_config.get("v5_error_correction", False)


def get_pysolarmanv5_instance():
    for attempt in range(retry_attempts):
        try:
            log.info("Attempting to connect to inverter")
            instance = PySolarmanV5(
                address,
                serial,
                port=port,
                mb_slave_id=mb_slave_id,
                socket_timeout=socket_timeout,
                v5_error_correction=v5_error_correction,
            )
        except Exception as e:
            log.info("Connection attempt failed: %s", e)
            continue
        else:
            log.info("Connected to inverter")
            return instance
    else:
        log.error("Connection failed; Retry limit exceeded")


@service
def pysolarmanv5_read_holding_registers(register_addr, quantity):
    """yaml
    name: pysolarmanv5.read_holding_registers()
    description: Read Holding Register (Modbus Function Code 3)
    fields:
      register_addr:
        description: register
        required: true
        selector:
         number:
             mode: box
      quantity:
        description: value
        required: true
        selector:
         number:
             mode: box
    """
    pysolarmanv5 = get_pysolarmanv5_instance()
    if pysolarmanv5 is not None:
        for attempt in range(retry_attempts):
            try:
                log.info("read_holding_registers(%s, %s)", register_addr, quantity)
                log.info(
                    pysolarmanv5.read_holding_registers(
                        register_addr=register_addr, quantity=quantity
                    )
                )
            except Exception as e:
                continue
            else:
                break
        else:
            log.error(
                "Failed to read_holding_registers(%s, %s)", register_addr, quantity
            )


@service
def pysolarmanv5_read_input_registers(register_addr, quantity):
    """yaml
    name: pysolarmanv5.read_input_registers()
    description: Read Input Register (Modbus Function Code 4)
    fields:
      register_addr:
        description: register
        required: true
        selector:
         number:
             mode: box
      quantity:
        description: value
        required: true
        selector:
         number:
             mode: box
    """
    pysolarmanv5 = get_pysolarmanv5_instance()
    if pysolarmanv5 is not None:
        for attempt in range(retry_attempts):
            try:
                log.info("read_input_registers(%s, %s)", register_addr, quantity)
                log.info(
                    pysolarmanv5.read_input_registers(
                        register_addr=register_addr, quantity=quantity
                    )
                )
            except Exception as e:
                continue
            else:
                break
        else:
            log.error("Failed to read_input_registers(%s, %s)", register_addr, quantity)


@service
def pysolarmanv5_write_holding_register(register_addr, value):
    """yaml
    name: pysolarmanv5.write_holding_register()
    description: Write Holding Register (Modbus Function Code 6)
    fields:
      register_addr:
        description: register
        required: true
        selector:
         number:
             mode: box
      value:
        description: value
        required: true
        selector:
         number:
             mode: box
    """
    pysolarmanv5 = get_pysolarmanv5_instance()
    if pysolarmanv5 is not None:
        for attempt in range(retry_attempts):
            try:
                log.info("write_holding_register(%s, %s)", register_addr, value)
                pysolarmanv5.write_holding_register(
                    register_value=register_addr, value=value
                )
            except Exception as e:
                continue
            else:
                break
        else:
            log.error("Failed to write_holding_register(%s, %s", register_addr, value)


@service
def pysolarmanv5_write_multiple_holding_registers(register_addr, values):
    """yaml
    name: pysolarmanv5.write_multiple_holding_registers()
    description: Write Multiple Holding Registers (Modbus Function Code 16)
    fields:
      register_addr:
        description: register
        required: true
        selector:
         number:
             mode: box
      values:
        description: values
        required: true
        example: |
         - 1
         - 2
         - 3
        selector:
         object:
    """
    pysolarmanv5 = get_pysolarmanv5_instance()
    if pysolarmanv5 is not None:
        for attempt in range(retry_attempts):
            try:
                log.info(
                    "write_multiple_holding_registers(%s, %s)", register_addr, values
                )
                pysolarmanv5.write_multiple_holding_registers(
                    register_value=register_addr, values=values
                )
            except Exception as e:
                continue
            else:
                break
        else:
            log.error(
                "Failed to write_multiple_holding_registers(%s, %s",
                register_addr,
                values,
            )
