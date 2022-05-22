package de.hadiko.vev.k2.bierboerse;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import androidx.recyclerview.widget.RecyclerView;

public class CustomAdapter extends RecyclerView.Adapter<CustomAdapter.ViewHolder> {

    private ListItem[] localDataSet;

    public static class ViewHolder extends RecyclerView.ViewHolder {
        private final TextView text_name;
        private final TextView text_price;
        private ListItem that;

        public ViewHolder(View view) {
            super(view);
            view.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (that instanceof ListItem.ListItem_Add) {
                        Toast.makeText(view.getContext(), "Adding",
                                Toast.LENGTH_LONG).show();
                    } else {
                        Toast.makeText(view.getContext(), text_name.getText(),
                                Toast.LENGTH_LONG).show();
                    }
                }
            });

            text_name = (TextView) view.findViewById(R.id.text_name);
            text_price = (TextView) view.findViewById(R.id.text_price);
        }

        public TextView getNameView() {
            return text_name;
        }

        public TextView getPriceView() {
            return text_price;
        }

        public void setThat(ListItem mThat) {
            that = mThat;
        }
    }

    public CustomAdapter(ListItem[] dataSet) {
        localDataSet = dataSet;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup viewGroup, int viewType) {
        View view = LayoutInflater.from(viewGroup.getContext())
                .inflate(R.layout.item_layout, viewGroup, false);

        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(ViewHolder viewHolder, final int position) {
        viewHolder.getNameView().setText(localDataSet[position].getName());
        viewHolder.getPriceView().setText(localDataSet[position].getCurrentPrice());
        viewHolder.setThat(localDataSet[position]);
    }

    @Override
    public int getItemCount() {
        return localDataSet.length;
    }
}

