const SerialPort = require('serialport');
const Readline = require('@serialport/parser-readline');
const port = new SerialPort('/COM6', { baudRate: 9600 });
const parser = port.pipe(new Readline({ delimiter: '\n' }));

function main() {
    let message;
    process.stdout.write("Enviar opcion a Arduino:\n");
    process.stdout.write("1: Encender - 2: Apagar\n");
    process.stdout.write("Ingrese su opcion:\n");
    process.stdin.on("data", function (data) {
        message = data.toString().trim();
        process.stdout.write(message);
        // Read the port data
        port.on("open", () => {
            console.log("serial port open");
        });

        port.write(message, (err) => {
            if (err) {
                return process.stdout.write('Error on write: ', err.message);
            }
            process.stdout.write('message written:' + message);
        });


        parser.on('data', data =>{
            process.stdout.write('got word from arduino:'+ data.toString());
        });

        port.on("close", () => {
            process.stdout.write('serial port close\n');
        });
        process.exit();
    })

}

main();


