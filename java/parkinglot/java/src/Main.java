public class Main {
    public static void main(String[] args) throws Exception {
        ParkingLot chiba = new ParkingLot();
        // User arrived
        VehicleUser vUser1 = new VehicleUser();
        vUser1.setData("Ayu", "987654321", "vehicleUser", "tok32", "NA");
        vUser1.getData();

        // CHeck availability
        chiba.isAvailable();

        // Genrate token
        Token token1 = new Token();
        System.out.println("New Token generated: " + token1.tokenNumber + " at " + token1.entryDate) ;

        // slot assignment
        System.out.println(vUser1.name + ", go to slot " + ParkingLot.takenSlots);
        Thread.sleep(5000);

        // exit
        token1.duration = token1.calculateDuration();
        System.out.println(vUser1.name + ", Please pay INR: " + token1.calculateCharge(token1.duration));
    }
}