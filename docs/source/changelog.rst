*********
Changelog
*********
Latest release

*********
**0.2.2**
*********
*Release date: Apr 26, 2020*

 * for correlation id and request id plugins, add support for enforcing the generation of a new value
 * for ^ plugins add support for validating uuid. It's a default behavior so will break things for people who don't use uuid4 there. If you don't want this validation, you need to pass validate=False to the plugin
 * thanks to @VukW you can now check if context is available

*********
**0.2.1**
*********
*Release date: Apr 18, 2020*

 * dropped with_plugins from the middleware as Starlette has it's own way of doing this
 * due to ^ this change some tests are simplified
 * if context is not available no LookupError will be raised, instead there will be RuntimeError, because this error might mean one of two things: user either didn't use ContextMiddleware or is trying to access context object outside of request-response cycle

*********
**0.2.0**
*********
*Release date: Feb 21, 2020*

 * changed parent of context object. More or less the API is the same but due to this change the implementation itself is way more simple and now it's possible to use .items() or keys() like in a normal dict, out of the box. Still, unpacking **kwargs is not supported and I don't think it ever will be. I tried to inherit from the builtin dict but nothing good came out of this. Now you access context as dict using context.data, not context.dict()
 * there was an issue related to not having awaitable plugins. Now both middleware and plugins are fully async compatible. It's a breaking change as it forces to use await, hence new minor version

*********
**0.1.6**
*********
*Release date: Jan 2, 2020*

 * breaking changes
 * one middleware, one context, multiple plugins for middleware
 * very easy testing and writing custom plugins

*********
**0.1.5**
*********
*Release date: Jan 1, 2020*

 * lint
 * tests (100% cov)
 * separate class for header constants
 * BasicContextMiddleware add some logic

*********
**0.1.4**
*********
*Release date: Dec 31, 2019*

 * get_many in context object
 * cicd improvements
 * type annotations

*******************
**mvp until 0.1.4**
*******************
 * experiments and tests with ContextVar