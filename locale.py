swagger: '2.0'
info:
  version: "2.0.0"
  title: Sample Application Flow OAuth2 Project
  description: This is an example of using OAuth2 Application Flow in a specification to describe security to your API.

 
# Under securityDefinitions we declare which security schemes can be used.
# These definitions do not affect to the operations, but can be applied
# using the 'security' key at the global level or the operation level.
# In this sample, we'll see how to apply the security definition globally,
# and override it at the operation level.
#
# Note that for Application Flow, you must provide the Token URL.
securityDefinitions:
  application:
    type: oauth2
    # This should be updated to the Token URL of your OAuth provider.
    tokenUrl: http://example.com/oauth/token
    flow: application
    scopes:
      write: allows modifying resources
      read: allows reading resources

# Here we apply the security flow called 'application' globally to all the opeartions in the spec. 
# This security scheme is defined above in the 'securityDefinitions' section.
# Global security can be overriden an operation level as seen in the example below
security:
  - application:
    - read
    - write
paths:
  /example:
    # In this operation we do not apply the security, because it was applied globally above.
    # The security will be applied to this operation for that reason.
    get:
      summary: Server example operation
      description: This is an example opeartion to show how security is applied to the call.
      responses:
        200:
          description: OK
  /ping:
    get:
      summary: Server heartbeat operation
      description: This operation shows how to override the global security defined above, as we want to open it up for all users.
      # We want to require no security schemes and override the globally define security scheme.
      # To do that, we simply provide an empty array to the 'security' property.
      security: [ ]
      responses:
        200:
          description: OK
# Added by API Auto Mocking Plugin
host: virtserver.swaggerhub.com
# basePath: /VSPL/test/2.0.0
schemes:
 - https
# Added by API Auto Mocking Plugin
basePath: /VSPL/test/2.0.0