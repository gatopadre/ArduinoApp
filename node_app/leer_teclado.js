function main() {
    let nombre;
    process.stdout.write("Escribe tu nombre\n");
    process.stdin.on("data", function (data) {
        nombre = data.toString().trim();
        process.stdout.write(nombre);
        process.exit();
    })

}

main();




