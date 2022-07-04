protected String obtenerJsonPersonalizado(String parcelaid, int estadoparcela) {
        int p = Integer.parseInt(parcelaid);
        if (p < 44)
            return "[{\"id\" : 0,\"adds\" : [ ], \"updates\": [ { \"attributes\": { \"OBJECTID\":" + parcelaid + ", \"Estado\":" + estadoparcela + ",} } ] } ]";

        if (p < 106)
            return "[{\"id\" : 0,\"adds\" : [ ], \"updates\": [ { \"attributes\": { \"OBJECTID\":" + (p - 38) + ", \"Estado\":" + estadoparcela + ",} } ] } ]";

        return "[{\"id\" : 0,\"adds\" : [ ], \"updates\": [ { \"attributes\": { \"OBJECTID\":" + (p - 39) + ", \"Estado\":" + estadoparcela + ",} } ] } ]";
    }
