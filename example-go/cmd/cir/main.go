package main

import (
	"flag"
	"fmt"
	"log"

	"github.com/go-openapi/loads"
	"github.com/go-openapi/runtime/middleware"
	"github.com/go-openapi/swag"

	"github.com/vbatts/example/gen/models"
	"github.com/vbatts/example/gen/restapi"
	"github.com/vbatts/example/gen/restapi/operations"
)

var portFlag = flag.Int("port", 3000, "Port to run this service on")

func main() {
	// load embedded swagger file
	swaggerSpec, err := loads.Analyzed(restapi.SwaggerJSON, "")
	if err != nil {
		log.Fatalln(err)
	}

	// create new service API
	api := operations.NewGreeterAPI(swaggerSpec)
	server := restapi.NewServer(api)
	defer func() {
		_ = server.Shutdown()
	}()

	// parse flags
	flag.Parse()
	// set the port this service will be run on
	server.Port = *portFlag

	// GetGreetingHandler greets the given name,
	// in case the name is not given, it will default to World
	api.GetGreetingHandler = operations.GetGreetingHandlerFunc(
		func(params operations.GetGreetingParams) middleware.Responder {
			name := swag.StringValue(params.Name)
			if name == "" {
				name = "World"
			}

			greeting := fmt.Sprintf("Hello, %s!", name)
			return operations.NewGetGreetingOK().WithPayload(greeting)
		})
	api.GetCIRHandler = operations.GetCIRHandlerFunc(
		func(params operations.GetCIRParams) middleware.Responder {

			// TODO lookup CIR info from a db backend
			c := models.CIR{
				BarcodeID: params.Barcode,
			}
			return operations.NewGetCIROK().WithPayload(&c)
		})

	// serve API
	if err := server.Serve(); err != nil {
		log.Fatalln(err)
	}
}
