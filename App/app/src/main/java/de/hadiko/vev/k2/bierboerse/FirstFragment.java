package de.hadiko.vev.k2.bierboerse;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import de.hadiko.vev.k2.bierboerse.databinding.FragmentFirstBinding;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class FirstFragment extends Fragment {

    private FragmentFirstBinding binding;

    private BierboerseGrpc.BierboerseBlockingStub stub;
    private ManagedChannel mChannel;

    private static final int DATASET_COUNT = 60;
    protected RecyclerView mRecyclerView;
    protected CustomAdapter mAdapter;
    protected RecyclerView.LayoutManager mLayoutManager;
    protected ListItem[] mDataset;

    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {

        binding = FragmentFirstBinding.inflate(inflater, container, false);

        mChannel = ManagedChannelBuilder.forAddress("100.124.87.221", 1337).usePlaintext().build();
        stub = BierboerseGrpc.newBlockingStub(mChannel);
        initDataset();

        mRecyclerView = (RecyclerView) binding.getRoot().findViewById(R.id.recyclerView);
        mLayoutManager = new LinearLayoutManager(getActivity());
        mRecyclerView.setLayoutManager(mLayoutManager);
        mAdapter = new CustomAdapter(mDataset);
        mRecyclerView.setAdapter(mAdapter);

        return binding.getRoot();
    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }

    private void initDataset() {
        BierboerseOuterClass.PricesRequest req = BierboerseOuterClass.PricesRequest.newBuilder().build();
        BierboerseOuterClass.Datapoint reply = stub.getPrices(req);
        mDataset = new ListItem[reply.getBeveragesCount() + 1];
        for (int i = 0; i < reply.getBeveragesCount(); i++) {
            mDataset[i] = new ListItem(reply.getBeverages(i).getName(), "" + reply.getBeverages(i).getCurrentPrice());
        }
        ListItem.ListItem_Add add = new ListItem().new ListItem_Add();
        add.setName("ADD");
        add.setCurrentPrice("ADD");
        mDataset[reply.getBeveragesCount()] = add;
    }
}