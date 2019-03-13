public class ParkingLot {
    static final int maxCapacity = 100;
    public static int takenSlots = 0;
    public static int availableSlots = maxCapacity;
    public void isAvailable() {
        System.out.println("Available slots:" + availableSlots);
        if(availableSlots > 0) {
            alotSlot();
        }
    }
    public void alotSlot() {
            takenSlots++;
            availableSlots--;
    }
    public void freeSlot() {
        if(takenSlots > 0) {
            takenSlots--;
            availableSlots++;
        }
    }
}