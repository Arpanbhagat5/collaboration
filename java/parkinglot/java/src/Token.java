import java.text.SimpleDateFormat;
import java.util.Date;

public class Token extends ParkingLot {
    public String tokenNumber;
    public Date entryDate;
    public Date exitDate;
    public double duration;
    Float charge;

    public Token(){
        entryDate = new Date();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyMMddHHmmss");
        tokenNumber = dateFormat.format(entryDate);
    }
    public double calculateDuration() throws Exception{
        exitDate = new Date();
        long diff = exitDate.getTime() - entryDate.getTime();
        return (double)(diff)/(1000*60*60*24);
    }
    public double calculateCharge(double duration) {
        double dayCharge = 10;
        //float hourCharge = 2;
        double charge = duration*dayCharge;
        freeSlot();
        return charge;
    }
}